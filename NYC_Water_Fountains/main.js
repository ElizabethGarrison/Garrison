/* CONSTANTS AND GLOBALS */
const width = window.innerWidth * 0.9,
  height = window.innerHeight * 0.7,
  margin = { top: 20, bottom: 50, left: 60, right: 40 };
  const key = {
    'Rectangular Fountain with Child Step': '#fdae61',
    'Circular Fountain': '#abd9e9',
    'Circular Fountain with Child Step and Overhang': '#2c7bb6',
    'Rectangular Fountain with Overhang': '#d7191c',
    'Wheelchair Accessible Fountain': '#ffffbf',
    'Water Bottle Stations, Etc.': '#bdbdbd',
  };
  const colorLegend = [
    { type: 'A', color: '#fdae61' }, // Rectangular Fountain with Child Step
    { type: 'B', color: '#abd9e9' }, // Circular Fountain
    { type: 'C', color: '#2c7bb6' }, // Circular Fountain with Child Step and Overhang
    { type: 'D', color: '#d7191c' }, // Rectangular Fountain with Overhang
    { type: 'E', color: '#ffffbf' }, // Wheelchair Accessible Fountain
    { type: 'Other', color: '#bdbdbd' }, // Water Bottle Stations, Etc.
  ];

// SHOW LOADING SCREEN FOR AT MOST 2.5 SECONDS
const loadingScreen = d3.select("#loading-screen")
  .style("display", "block");
setTimeout(() => {
  loadingScreen.style("display", "none");

  /*LOAD DATA*/
  Promise.all([
    d3.json("../data/Borough_Boundaries.geojson"),
    d3.csv("../data/DrinkingFountains_20190417.csv", d3.autoType),
  ]).then(([geojson, drinkingFountains]) => {
    console.log('drinkingFountains', drinkingFountains);

    const svg = d3.select("#container")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    svg.append("text")
      .attr("x", (width / 3.5))
      .attr("y", margin.top * 2)
      .attr("text-anchor", "middle")
      .style("font-size", "20px")
      .style("font-weight", "bold")
      .style("fill", "#08415C")
      .text("NYC Drinking Fountains");

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
      .attr("stroke", "#08415C");

// APPEND DATA AS SHAPE
const drinkingFountainsShapes = svg.selectAll("circle.drinkingFountainsShapes")
  .data(drinkingFountains)
  .join("circle")
  .attr("class", d => "drinkingFountainsShapes type-" + (d.TYPE ? d.TYPE.replace(/\s+/g, '-') : 'Other'))
  .attr("r", 4)
  .attr("transform", (d) => {
    const [x, y] = projection([d.Long, d.Lat]);
    return `translate(${x}, ${y})`;
  })
  .attr("fill", d => key[d.TYPE] || key.Other)
  .on("mouseover", function (event, d) {
    const tooltip = d3.select("#tooltip");
    tooltip.style("display", "block");
    tooltip.html(`<p><strong>Description:</strong> ${d.DESCRIPTION}</p><p><strong>Sign Name:</strong> ${d.SIGNNAME}</p>`);
    const parentPos = this.parentNode.getBoundingClientRect();
    tooltip.style("left", event.offsetX + parentPos.left - 150 + "px");
    tooltip.style("top", event.offsetY + parentPos.top - 150 + "px"); 
  })
  .on("mouseout", function () {
    const tooltip = d3.select("#tooltip");
    tooltip.style("display", "none");
  });

// CREATE LEGEND
const legendMargin = 20;
const legend = svg.append("g")
  .attr("class", "legend")
  .attr("transform", `translate(${width - margin.right - 300 - legendMargin}, ${margin.top + legendMargin})`);

const legendKeys = Object.keys(key);

legendKeys.forEach((k, i) => {
  const legendRow = legend.append("g")
    .attr("transform", `translate(0, ${i * 20})`);

  legendRow.append("rect")
    .attr("width", 10)
    .attr("height", 10)
    .attr("fill", key[k]);

    legendRow.append("text")
    .attr("x", 16)
    .attr("y", 10)
    .text(k);  
});

  });
}, 2500); // 2.5 SECOND DELAY BEFORE LOADING THE MAP
