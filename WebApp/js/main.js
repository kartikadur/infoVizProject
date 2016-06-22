(function(window, document, d3, undefined) {
  var width = 880,
    height = 600,
    cellsize = 35,
    border = 1;

  var color = d3.scale.category20();

  var svg = d3.select('body')
              .append('svg')
              .attr({
                'width': width,
                'height': height
              });

  d3.csv('data/csvOutput.csv', function(error, csv) {


    var episode = svg.selectAll('.episode')
              .data(csv)
              .enter()
              .append('g')
              .attr({
                'class': 'episode',
                'x': function(d) { return d.seasonEpisodeNumber * cellsize + cellsize;},
                'y': function(d) { return d.seasonNumber * cellsize;},
              });


      episode.append('rect')
              .attr({
                'width': cellsize,
                'height': cellsize,
                'x': function(d) { return d.seasonEpisodeNumber * cellsize + cellsize;},
                'y': function(d) { return d.seasonNumber * cellsize;},
                'fill': function(d) { return color(d.seasonNumber); },
                'stroke-width': border,
                'stroke': 'whitesmoke',
                'title' : function(d) {return d.showTitle;}
              });

      episode.append('text')
              .attr({
                'class' : 'title',
                'x' : function(d) { return d.seasonEpisodeNumber * cellsize + 1.5 * cellsize; },
                'y' : function(d) { return d.seasonNumber * cellsize + 0.6 * cellsize; }
              })
              .text(function(d) { return d.seasonEpisodeNumber; });


      svg.selectAll('.y-axis')
              .data(d3.range(0,16))
              .enter()
              .append('text')
              .attr({
                'class': 'y-axis',
                'x': function(d) { return cellsize; },
                'y': function(d) { return d * cellsize; },
                'dy': function(d) { return 0.65 * cellsize; }
              })
              .text(function(d) { 
                if(d === 0){
                  return 'Season';
                } else {
                  return d;
                }});


  });

})(window, document, d3);