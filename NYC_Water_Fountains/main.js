/* CONSTANTS AND GLOBALS */
const width = window.innerWidth * 0.9,
 height = window.innerHeight * 0.7,
 margin = { top: 20, bottom: 50, left: 60, right: 40 };

// Show loading screen
const loader = d3.select("body").append("div")
  .attr("id", "loader")
  .style("display", "flex")
  .style("justify-content", "center")
  .style("align-items", "center");
  
loader.append("div")
  .attr("class", "spinner");
  
loader.append("div")
  .attr("class", "text")
  .text("Loading...");

/**
 * LOAD DATA
 * Using a Promise.all([]), we can load more than one dataset at a time
 * */
 Promise.all([
  d3.json("../data/Borough_Boundaries.geojson"),
  d3.csv("../data/Cool_It__NYC_2020_-_Cooling_Sites.csv", d3.autoType),
]).then(([geojson, coolingSites]) => {

  console.log('coolingSites', coolingSites)

  const svg = d3.select("#container")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

  svg.append("text")
  .attr("x", (width / 2))             
  .attr("y", margin.top * 2)
  .attr("text-anchor", "middle")  
  .style("font-size", "20px") 
  .style("font-weight", "bold") 
  .style("fill", "#08415C") 
  .text("NYC Cooling Sites");

  
  // SPECIFY PROJECTION
  const projection = d3.geoMercator()
    .fitSize([width, height], geojson)

   // DEFINE PATH FUNCTION
  const pathGen = d3.geoPath(projection)

    // APPEND GEOJSON PATH  
  const boroughs = svg.selectAll("path.boroughs")
    .data(geojson.features)
    .join("path")
    .attr("class", "boroughs")
    .attr("d", coords => pathGen(coords))
    .attr("fill", "#EEE5E9") 
    .attr("stroke", "#08415C")

// APPEND DATA AS SHAPE
const coolingSitesShapes = svg.selectAll("circle.coolingSitesShapes")
  .data(coolingSites)
  .join("circle")
  .attr("class", "coolingSitesShapes")
  .attr("r", 5)
  .attr("transform", d => {
    const [x, y] = projection([d.Longitude, d.Latitude])
    return `translate(${x}, ${y})`
  })  
  .attr("fill", "#CC2936");


  // ADD TOOLTIP
  const tooltip = d3.select("#container")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0)

  coolingSitesShapes.on("mouseover", function(d) {
    tooltip.transition()
      .duration(200)
      .style("opacity", .9);
    tooltip.html(`
      <div>Property Name: ${d.PropertyName}</div>
      <div>Feature Type: ${d.FeatureType}</div>
      <div>Status: ${d.Status}</div>
    `)
      .style("left", (d3.event.pageX + 20) + "px")
      .style("top", (d3.event.pageY - 28) + "px");
  })
  .on("mouseout", function(d) {
    tooltip.transition()
      .duration(500)
      .style("opacity", 0);
  });
  // Get the input field and button elements from the DOM
const inputField = document.getElementById('input-field');
const submitButton = document.getElementById('submit-button');

// Add an event listener to the button element
submitButton.addEventListener('click', function() {
  // Get the value of the input field
  const inputText = inputField.value;
  
  // Log the input text to the console
  console.log(inputText);
});

});
