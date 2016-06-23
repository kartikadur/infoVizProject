(function(window, document, d3, undefined) {

  var height = 36,
	  width = 960,
	  margin = {top: 10, right: 10, bottom: 10, left: 10},
	  cell = 30;

	 var dateFormat = d3.time.format('%d/%m/%Y');

  var color = d3.scale.category20();

  var svg = d3.select('body').selectAll('.season')
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

  d3.csv("data/csvOutput.csv", function(error, csv) {

    	var data = d3.nest()
    					.key(function(d) {return d.seasonNumber; })
    					.map(csv);

    	var yAxisText = svg.append('text')
    					.attr({
    						'class' : 'seasonID',
    						'x' : cell / 2,
    						'y' : 0.6 * height
    					})
    					.text(function(d) { return d; })

    	var episodes = svg.selectAll('.episodes')
							.data(function(d) { return data[d]; })
							.enter()
							.append('rect')
							.attr({
								'class' : 'episodes',
								'x' : function(d) { return d.seasonEpisodeNumber * cell; },
								'y' : function(d) { return (height - cell) / 2;},
								'width' : cell,
								'height' : cell
							})
							.on('mouseover', function(d) {
								pointer = d3.event
								tooltip.style('visibility', 'visible');
								
								tooltip.transition()
										.duration(200)
										.style('opacity', 0.95)

								tooltip.html(
									'<h3>Title: ' + d.showTitle + '</h3>'
									+ '<p> Original Air Date: ' + dateFormat(new Date(d.airDate)) + '</p>'
									)
										.style({
											'left' : pointer.pageX + 25 + 'px',
											'top' : pointer.pageY + 'px'
										});

							})
							.on('mouseout', function(d) {
								tooltip.transition()
										.duration(150)
										.style({
											'opacity' : 0
										});
							});
  });

})(window, document, d3)