socket = io.connect "http://#{window.location.hostname}:#{window.location.port}"

$ ->
	$main = $ '#main-input'
	$back = $ '#back-input'

	waiting = false
	conflict = false
	seed = ''

	emit = ->
		waiting = true
		seed = $main.val().toLowerCase()
		socket.emit 'predict', seed

	apply = (prediction)->
		$back.val seed+prediction
		if conflict
			conflict = false
			emit()
		else
			waiting = false

	$main.on 'input', ->
		if waiting
			conflict = true
			return
		emit()

	socket.on 'predicted', (prediction) ->
		apply(prediction)

	$main.on 'keypress', (e) ->
		if e.keyCode == 13
			$main.val $back.val()
			$main.trigger 'input'