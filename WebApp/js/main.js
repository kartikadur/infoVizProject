(function(window, document, d3, undefined) {
	var margin = 10,
		width = window.innerWidth - 2 * margin,
		height = window.innerHeight - 2* margin,
		radius = 20;

	var color = d3.scale.category20();

	var force = d3.layout
					.force()
					.gravity(0.05)
					.charge(-10)
					.linkDistance(30)
					.size([width, height]);

	var svg = d3.select('body')
				.append('svg')
				.attr('width', width)
				.attr('height', height);

	d3.json("js/data.json", function(error, graph) {
		if (error) throw error;

		console.log(graph);
		force
			.nodes(graph.nodes)
			.links(graph.links)
			.start()

		var link = svg.selectAll('.link')
						.data(graph.links)
						.enter()
						.append("line")
						.attr("class", "link")
						.style("stroke-width", function(d){ return Math.sqrt(d.value); });

		var node = svg.selectAll('.node')
						.data(graph.nodes)
						.enter()
						.append('rect')
						.attr('class','node')
						.attr('width', radius)
						.attr('height', radius)
						.style('fill', function(d) { return color(d.group); });

		node.append('title')
			.text(function(d) { return d.name; });

		force.on("tick", function() {
		    link.attr("x1", function(d) { return d.source.x + radius/2; })
		        .attr("y1", function(d) { return d.source.y + radius/2; })
		        .attr("x2", function(d) { return d.target.x + radius/2; })
		        .attr("y2", function(d) { return d.target.y + radius/2; });

		    // node.attr("cx", function(d) { return d.x; })
		    //     .attr("cy", function(d) { return d.y; });

		    node.attr("x", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
		        .attr("y", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });

			});

	});

})(window, document, d3);