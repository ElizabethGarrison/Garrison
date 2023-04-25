/* CONSTANTS AND GLOBALS */
const width = window.innerWidth * 0.9,
  height = window.innerHeight * 0.7,
  margin = { top: 20, bottom: 50, left: 60, right: 40 };

// SHOW LOADING SCREEN FOR AT MOST 4 SECONDS
const loadingScreen = d3.select("#loading-screen")
  .style("display", "block");
setTimeout(() => {
  loadingScreen.style("display", "none");

/*LOAD DATA*/
Promise.all([
  d3.json("../data/mergedfile_Fountains_Boundaries.geojson",),
  d3.csv("../data/DrinkingFountains_20190417.csv", d3.autoType),
]).then(([geojson, drinkingFountains, nycParksDrinkingFountains]) => {
  console.log('drinkingFountains', drinkingFountains);
  console.log('nycParksDrinkingFountains', nycParksDrinkingFountains);

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
    .attr("stroke", "#08415C")

  // APPEND DATA AS SHAPE
  const drinkingFountainsShapes = svg.selectAll("circle.drinkingFountainsShapes")
    .data(drinkingFountains)
    .join("circle")
    .attr("class", "drinkingFountainsShapes")
    .attr("r", 5)
    .attr("transform", (d) => {
      const [x,y] = projection([d.Long,d.Lat])
      return `translate(${x}, ${y})`
    })
    .attr("fill", "#6baed6");

  });
}, 2500); //4 SECOND DELAY BEFORE LOADING THE MAP