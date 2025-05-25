<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div class="library-list">
      <h3>주변 도서관</h3>
      <ul>
        <li v-for="(place, index) in places" :key="index">
          <a
            :href="`https://www.google.com/maps/search/?api=1&query=${place.name}&query_place_id=${place.place_id}`"
            target="_blank"
          >
            {{ place.name }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const API_KEY = import.meta.env.VITE_MAP_API_KEY
const map = ref(null)
const places = ref([])
let markers = []

const clearMarkers = () => {
  markers.forEach((marker) => marker.setMap(null))
  markers = []
}

const searchNearbyLibraries = (lat, lng) => {
  const service = new google.maps.places.PlacesService(map.value)
  const request = {
    location: { lat, lng },
    radius: 2000,
    keyword: '도서관',
  }

  service.nearbySearch(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK && results) {
      places.value = results
      clearMarkers()

      results.forEach((place) => {
        const marker = new google.maps.Marker({
          map: map.value,
          position: place.geometry.location,
          title: place.name,
        })
        markers.push(marker)
      })
    }
  })
}

const initMap = (lat, lng) => {
  map.value = new google.maps.Map(document.getElementById('map'), {
    center: { lat, lng },
    zoom: 15,
  })

  searchNearbyLibraries(lat, lng)

  map.value.addListener('idle', () => {
    const center = map.value.getCenter()
    searchNearbyLibraries(center.lat(), center.lng())
  })
}

const getCurrentLocation = () => {
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const { latitude, longitude } = pos.coords
      initMap(latitude, longitude)
    },
    (err) => {
      alert('위치 정보를 가져올 수 없습니다: ' + err.message)
    }
  )
}

onMounted(() => {
  if (!window.google) {
    const script = document.createElement('script')
    script.src = `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&libraries=places`
    script.async = true
    script.defer = true
    script.onload = getCurrentLocation
    document.head.appendChild(script)
  } else {
    getCurrentLocation()
  }
})
</script>

<style scoped>
.map-container {
  display: flex;
  flex-direction: row;
  max-width: 1000px;
  margin: 2rem auto;
  gap: 1rem;
}

.map {
  width: 70%;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.library-list {
  width: 30%;
  overflow-y: auto;
  max-height: 500px;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
}

.library-list ul {
  list-style: none;
  padding: 0;
}

.library-list li {
  margin-bottom: 1rem;
}

.library-list a {
  color: #2563eb;
  text-decoration: none;
}
</style>
