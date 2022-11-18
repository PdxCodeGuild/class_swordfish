

require(
    [
    "esri/config",
    "esri/Map",
    "esri/views/MapView",
    "esri/Graphic",
    "esri/layers/GraphicsLayer",
    "esri/geometry/Multipoint",
    ],

    function(esriConfig, Map, MapView, Graphic, GraphicsLayer, Multipoint) {
        esriConfig.apiKey = "AAPKa69c01d84be143d2aed0ad78c6386646fab0glupksy3eawHfYb4yW1TrjMS8hwjuF8YpsVqpzPfq0xCKaz-k-sIq9hXymW9";
        const map = new Map({
            basemap: "arcgis-topographic" // basemap layer service
        })
        const graphicsLayer = new GraphicsLayer()
        map.add(graphicsLayer)
        const view = new MapView({
            map: map,
            center: [-122.6784,45.5152], // long, lat
            zoom: 13,
            container: "viewDiv"
        })

        function createMultipointGraphic(vertices) {
            // view.graphics.removeAll();

            let multipoint = new Multipoint({
                points: vertices,
                spatialReference: view.spatialReference
            });

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
                geometry: multipoint,
                symbol: simpleMarkerSymbol,
                attributes: attributes,
                popupTemplate: popupTemplate,
            });
            view.graphics.add(graphic);
        }

        let testingVertices = [[-122.691005,45.512555],[-122.6784,45.5152]]
        createMultipointGraphic(testingVertices)

        function collapseOldStuff() {


        
        // const point = {
        //     type: "point",
        //     longitude: -122.691005,
        //     latitude: 45.512555,
        // }

        // const jackPoint = {
        //     type: "point",
        //     longitude: -122.691005,
        //     latitude: 45.512555,
        // }

        // const pointGraphic = new Graphic({
        //     geometry: jackPoint,
        //     symbol: simpleMarkerSymbol,
        //     attributes: attributes,
        //     popupTemplate: popupTemplate,
        // })

     
        }
    }
)


