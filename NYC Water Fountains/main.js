// Set the dimensions of the canvas
var margin = {top: 20, right: 20, bottom: 20, left: 20},
	width = window.innerWidth - margin.left - margin.right,
	height = window.innerHeight - margin.top - margin.bottom;

// Set the map projection
var projection = d3.geoMercator()
	.center([-73.94, 40.70])
	.scale(60000)
	.translate([width / 2, height / 2]);

// Create a path generator
var path = d3.geoPath()
	.projection(projection);

// Create the SVG element
var svg = d3.select("#map").append("svg")
	.attr("width", width)
	.attr("height", height);

// Create a tooltip
var tooltip = d3.tip()
	.attr("class", "d3-tip")
	.offset([-10, 0])
	.html(function(d) {
		return "<strong>Property Name:</strong> " + d.PropertyName + "<br>" + "<strong>Feature Type:</strong> " + d.FeatureType + "<br>" + "<strong>Status:</strong> " + d.Status;
	});
svg.call(tooltip);

// Load the data
d3.csv("Cool_It__NYC_2020_-_Cooling_Sites.csv", function(data) {
	// Draw the map
	d3.json("nyc_boroughs.geojson", function(error, json) {
		if (error) throw error;
		svg.append("g")
			.attr("class", "boroughs")
			.selectAll("path")
			.data(json.features)
			.enter().append("path")
			.attr("d", path);

		// Draw the data points
		svg.append("g")
			.attr("class", "points")
			.selectAll("circle")
			.data(data)
			.enter().append("circle")
			.attr("class", "circle")
			.attr("r", 5)
			.attr("cx", function(d) { return projection([d.X, d.Y])[0]; })
			.attr("cy", function(d) { return projection([d.X, d.Y])[1]; })
			.on("mouseover", function(d) {
				tooltip.show(d);
			})
			.on("mouseout", function(d) {
				tooltip.hide(d);
			});
	});

	// Remove the loading screen
	$("#loader-wrapper").fadeOut();
});
