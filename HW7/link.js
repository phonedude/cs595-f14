var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d){return Math.log(d.value)})
      .style("stroke", function(d) { return lcolor(Math.exp(d.value) + 10)});

