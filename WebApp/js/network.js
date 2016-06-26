(function(window, document, d3, undefined) {

	var width = 960,
	height = 800,
	cell = 10;

	var color = d3.scale.category20();

	var svg = d3.select('#network_episodes')
	.append('svg')
	.attr({
		'width': width,
		'height':height
	});

	var force = d3.layout.force()
	.charge(-150)
	.linkDistance(30)
	.size([width, height]);

	d3.json('data/textNetwork.json', function(error, graph){
		if(error) throw error;


		var nodeById = d3.map();

		graph.nodes.forEach(function(node) {
			nodeById.set(node.id, node);
		});

		graph.links.forEach(function(link) {
			link.source = nodeById.get(link.source);
			link.target = nodeById.get(link.target);
		})

		// console.log(nodeById);

		force.nodes(graph.nodes)
		.links(graph.links)
		.start();

		var links = svg.selectAll('.link')
		.data(graph.links)
		.enter()
		.append('line')
		.attr({
			'class' : 'link',
			'stroke' : 'black'
		});

		var nodes = svg.selectAll('.node')
		.data(graph.nodes)
		.enter()
		.append('rect')
		.attr({
			'class' : 'node',
			'width' : cell,
			'height' : cell,
			'fill' : function(d) { return color(d.group); },
			'title' : function(d) { return d.name; }
		})
		.call(force.drag);

		force.on('tick', function() {
			links.attr({
				'x1': function(d) { return d.source.x; },
				'y1': function(d) { return d.source.y; },
				'x2': function(d) { return d.target.x; },
				'y2': function(d) { return d.target.y; }
			});

			nodes.attr({
				'x': function(d) { return d.x - cell / 2; },
				'y': function(d) { return d.y - cell / 2; }
			});

		});
	});

})(window, document, d3);