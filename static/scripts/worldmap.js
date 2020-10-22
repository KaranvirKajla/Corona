console.log("worldmap");
let url = "https://www.trackcorona.live/api/countries";

let maxconfirmed = 7244184

async function updateData() {
    let response = await fetch(url)
    if(response.ok){
        let parsed = await response.json();
        
        let rsp = parsed.data
        console.log(rsp[0])

        rsp.forEach(element => {
            let confirmed = element.confirmed;
            let longitude = element.longitude;
            let latitude = element.latitude;
            let temp = Math.round(confirmed/maxconfirmed)
            
            
            
            console.log(temp)
            new mapboxgl.Marker({
                draggable: false,
                color: `rgba(255,0,0,${temp})`
                })
                .setLngLat([longitude, latitude])
                .addTo(map);

        });

    }else{
        console.log("ERROR");
    }
}

mapboxgl.accessToken = 'pk.eyJ1Ijoia2FyYW52aXJrYWpsYSIsImEiOiJja2ZqZnJjMjAwNmtyMnFtZ2o2MGlqMjc3In0.I4o2fnxnklXLRjnB04oJyw';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center:[80,80],
zoom:2
});



updateData()



