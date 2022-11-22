
let vm = new Vue({
    el: "#app",
    data: {
        loading: false,
        geojson: {},
        points: [],
        testPoints: [[-122.6784,45.5152],],
        // const fileSelector = document.getElementById('file-selector');
    },
    methods: {
        loadMap: function(points = [], geojson = {}) {
            require(
                [
                "esri/config",
                "esri/Map",
                "esri/views/MapView",
                "esri/Graphic",
                "esri/layers/GraphicsLayer",
                // "esri/geometry/Multipoint",
                "esri/layers/GeoJSONLayer",
                ],
            
                function(esriConfig, Map, MapView, Graphic, GraphicsLayer, GeoJSONLayer) {
                    esriConfig.apiKey = "AAPKa69c01d84be143d2aed0ad78c6386646fab0glupksy3eawHfYb4yW1TrjMS8hwjuF8YpsVqpzPfq0xCKaz-k-sIq9hXymW9";
                    const map = new Map({
                        basemap: "arcgis-topographic" // basemap layer service
                    })
                    const graphicsLayer = new GraphicsLayer()
                    map.add(graphicsLayer)
                    const view = new MapView({
                        map: map,
                        center: [-122.6784,45.5152], // long, lat
                        zoom: 11,
                        container: "viewDiv"
                    })
                    view.popup.defaultPopupTemplateEnabled = true
                    
                    // takes [long, lat], creates new point graphic, and adds to view
                    // used for user location plotting
                    function createPoint(vertices) {
                        // view.graphics.removeAll();
            
                        const point = { //Create a point
                            type: "point",
                            longitude: vertices[0],
                            latitude: vertices[1],
                        }
            
                        const simpleMarkerSymbol = {
                            type: "simple-marker",
                            color: [226, 119, 40],
                            outline: {
                                color: [255, 255, 255],
                                width: 1
                            },
                        }
            
                        const attributes = {
                            Name: "JackHouse",
                            Description: "I am jacks house"
                        }
            
                        const popupTemplate = {
                            title: "{Name}",
                            content: "{Description}"
                        }
                            
                        graphic = new Graphic({
                            geometry: point,
                            symbol: simpleMarkerSymbol,
                            attributes: attributes,
                            popupTemplate: popupTemplate,
                        })
                        view.graphics.add(graphic)
                    }
                    if (JSON.stringify(points) !== JSON.stringify([])) {
                        for (let vertices of points) { // multiple points are used instead of multipoint object because I can't figure out how to add attributes to multipoint nodes
                            createPoint(vertices)
                        }
                    }

                    // loads geojson from current directory, and adds to view
                    // used for loaded geojson plotting
                    if (JSON.stringify(geojson) !== JSON.stringify({})) {
                        const blob = new Blob([JSON.stringify(geojson)], {
                            type: "application/json"
                        })
                        console.log(JSON.stringify(geojson))

                        const url = URL.createObjectURL(blob)

                        const geojsonlayer = new GeoJSONLayer({
                            url,
                        })

                        map.add(geojsonlayer)
                    }
                }
            )
        },
        showUsers: function() {
            axios({
                method: "GET",
                url: "https://jsonplaceholder.typicode.com/users",
            }).then((response) => {
                for (let user of response.data) {
                    let point = [parseFloat(user['address']['geo']['lng']),parseFloat(user['address']['geo']['lat'])]
                    this.points.push(point)
                }
                this.loadMap(points = this.points)
            })
        },
        showGeoJSON: function() {
            fetch('load.geojson')
            .then(res => res.json())
            .then(json => {
                this.loadMap(points = [], geojson = json)
            })

        },
        readFile(event) {
            const file = event.target.files[0]
            const reader = new FileReader()
            reader.onload = e => {
                let contents = e.target.result
                console.log(contents)
                geojson = JSON.parse(contents)
                this.loadMap(points = [], geojson = geojson)
            }
            reader.readAsText(file)
            
        }
        
    },

    beforeMount: function() {
        // this.showUsers()
        this.showGeoJSON()
    },

})

