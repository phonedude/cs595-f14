var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter().append("circle")
      .attr("class", "node")
      .attr("r", 10)
      .text(function(d){ return d.name})
      .style("fill", "gray")

