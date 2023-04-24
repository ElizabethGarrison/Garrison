$(document).ready(function(){
    // Show loading screen
    $("#loading").fadeIn();

    // Load data set
    d3.csv("data/Cool_It__NYC_2020_-_Cooling_Sites.csv", d3.autoType).then(function(data) {
        // Hide loading screen
        $("#loading").fadeOut();

        // Initialize map
        var width = window.innerWidth;
        var height = window.innerHeight;
        var svg = d3.select("#map").append("svg")
            .attr("width", width)
            .attr("height", height);
        var projection = d3.geoMercator()
            .scale(65000)
            .center([-73.94, 40.7]);
        var path = d3.geoPath().projection(projection);

        // Load boroughs
        d3.json("https://gist.githubusercontent.com/deldersveld/94bcbb7250bad11c4ddab154eea4f0ba/raw/171f0b7c8dc6e4e6d1efb2a55b76e8d6401ad6fc/nyc-boroughs.geojson").then(function(json) {
            svg.selectAll("path")
                .data(json.features)
                .enter()
                .append("path")
                .attr("d", path)
                .style("fill", "#ccc")
                .style("stroke", "#000")
                .style("stroke-width", 1);

            // Load data points
            var g = svg.append("g");
            var points = g.selectAll("circle")
                .data(data)
                .enter()
                .append("circle")
                .attr("cx", function(d) {
                    return projection([d.X, d.Y])[0];
                })
                .attr("cy", function(d) {
                    return projection([d.X, d.Y])[1];
                })
                .attr("r", 5)
                .style("fill", "#f00")
                .style("stroke", "#fff")
                .style("stroke-width", 1)
                .on("mouseover", function(d) {
                    var tooltip = tippy(this, {
                        content: "<b>" + d.PropertyName + "</b><br>" +
                            "Feature Type: " + d.FeatureType + "<br>" +
                            "Status: " + d.Status,
                        allowHTML: true,
                        placement: "top",
                        maxWidth: "none",
                        theme: "light-border"
                    });
                    tooltip.show();
                })
                .on("mouseout", function(d) {
                    tippy(this).hide();
                });

            // Add zoom and pan
            svg.call(d3.zoom()
                .scaleExtent([1, 8])
                .on("zoom", function() {
                    g.attr("transform", d3.event.transform);
                }));
        });
    });
});
