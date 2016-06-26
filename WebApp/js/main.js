(function(window, document, d3, undefined) {

	var height = 30,
	width = 580,
	margin = {top: 10, right: 10, bottom: 10, left: 10},
	cell = 25;

	var dateFormat = d3.time.format('%d/%m/%Y');

	var color = d3.scale.category20();

	var svg = d3.select('#linear_episodes').selectAll('.season')
	.data(d3.range(1, 16))
	.enter()
	.append('svg')
	.attr({
		'class' : 'season',
		'width' : width,
		'height' : height
	});

	var tooltip = d3.select('body')
	.append('div')
	.attr({
		'id' : 'tooltip',
	})
	.style({
		'position' : 'absolute',
		'visibility' : 'hidden',
		'z-index' : 10,
		'margin' : '5px',
		'padding' : '5px'
	});

	var year_selector = d3.select('#linear_controls').selectAll('.year_selector')
		.data(d3.range(1999, 2011))
		.enter()
		.append('button')
		.attr({
			'class' : 'year_selector',
		})
		.classed('selected', false)
		.text(function(d) { return d; });

	var clear_selection = d3.select("#linear_controls")
		.append('button')
		.attr({
			'class' : 'clear'
		})
		.classed('selected', true)
		.text('No selections');


	d3.json('data/goodEatsJSONData.json', function(error, json) {

		var yAxisText = svg.append('text')
		.attr({
			'class' : 'seasonID',
			'x' : cell / 2,
			'y' : 0.6 * height
		})
		.text(function(d) { return d; })

		var episodes = svg.selectAll('.episodes')
		.data(function(d) { return json[d]; })
		.enter()
		.append('rect')
		.attr({
			'class' : function(d) { return 'episodes yr_' + new Date(d.airDate).getFullYear(); },
			'x' : function(d) { return d.seasonEpisodeNumber * cell; },
			'y' : function(d) { return (height - cell) / 2;},
			'width' : cell,
			'height' : cell
		})
		.classed('active', true)
		.on('mouseover', function(d) {
			pointer = d3.event
			tooltip.style('visibility', 'visible');

			rString = '';
			d.recipeList.forEach(function(item) {
				rString += '<li>' + item + '</li>';
			});

			tString = ''
			d.topicList.forEach(function(item){
				tString += item + ', '
			});

			tString = tString.substring(0, tString.length - 2)

			tooltip.html(
				'<h3>Title: ' + d.showTitle + '</h3>'
				+ '<p> Original Air Date: ' + dateFormat(new Date(d.airDate)) + '</p>'
				+ '<ol>' + rString + '</ol>'
				+ '<p>' + tString + '</p>'
				)

			tooltip.style({
				'left' : function(d) { 
					if (tooltip[0][0].clientWidth + pointer.pageX + 50 >= window.innerWidth){
						return pointer.pageX - tooltip[0][0].clientWidth - 40 + 'px';
					} else {
						return pointer.pageX + 25 + 'px'; 
					}                                           
				},
				'top' : function(d) {
					if (tooltip[0][0].clientHeight + pointer.pageY + 20 >= window.innerHeight){
						return pointer.pageY - tooltip[0][0].clientHeight + 'px';
					} else {
						return pointer.pageY - 25 + 'px'; 
					}
					pointer.pageY + 'px'
				}
			});

			tooltip.transition()
			.duration(250)
			.style({
				'opacity': 0.95
			});



		})
		.on('mouseout', function(d) {
			tooltip.transition()
			.duration(250)
			.style({
				'opacity' : 0
			});

			tooltip.style({
				'left' : '-500px',
				'top' : '-500px'
			});
		});

		year_selector.on('click', function(d) {
			
			d3.selectAll('#linear_controls button').classed('selected', false)

			d3.select(this).classed('selected', true)

			// Set all episodes as inactive
			d3.selectAll('.episodes').classed('active', false);

			// Set appropriate classes active
			d3.selectAll('.yr_' + d).classed('active', true);
		});

		clear_selection.on('click', function(d) {

			d3.selectAll('#linear_controls button').classed('selected', false)

			d3.select(this).classed('selected', true)

			// Set all episodes as active
			d3.selectAll('.episodes').classed('active', true);

		});

	});

})(window, document, d3);