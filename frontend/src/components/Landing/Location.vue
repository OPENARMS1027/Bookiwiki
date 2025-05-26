<template>
  <div class="location-section">
    <div class="section-header">
      <h2 class="section-title">
        <i class="fas fa-map-marked-alt"></i>
        내 주변 도서관
      </h2>
      <p class="section-description">가까운 도서관을 찾아보세요</p>
    </div>
    <div class="map-container">
      <div class="map-wrapper">
        <div id="map" class="map"></div>
        <div class="map-overlay">
          <div class="search-radius">
            <i class="fas fa-search-location"></i>
            <span>2km 반경 내 도서관</span>
          </div>
        </div>
      </div>
      <div class="library-list">
        <div class="list-header">
          <h3>
            <i class="fas fa-list-ul"></i>
            주변 도서관 목록
          </h3>
        </div>
        <div class="list-content">
          <div v-if="places.length === 0" class="no-results">
            <i class="fas fa-info-circle"></i>
            <p>검색된 도서관이 없습니다</p>
          </div>
          <ul v-else>
            <li v-for="(place, index) in places" :key="index" class="library-item">
              <div class="library-info">
                <h4>{{ place.name }}</h4>
                <p v-if="place.vicinity" class="vicinity">
                  <i class="fas fa-location-dot"></i>
                  {{ place.vicinity }}
                </p>
              </div>
              <a
                :href="`https://www.google.com/maps/search/?api=1&query=${place.name}&query_place_id=${place.place_id}`"
                target="_blank"
                class="directions-button"
              >
                <i class="fas fa-directions"></i>
                길찾기
              </a>
            </li>
          </ul>
        </div>
      </div>
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
          animation: google.maps.Animation.DROP
        })
        markers.push(marker)
      })
    }
  })
}

const initMap = (lat, lng) => {
  const mapOptions = {
    center: { lat, lng },
    zoom: 15,
    styles: [
      {
        featureType: "poi",
        elementType: "labels",
        stylers: [{ visibility: "off" }]
      },
      {
        featureType: "poi.park",
        elementType: "labels",
        stylers: [{ visibility: "on" }]
      }
    ]
  }
  
  map.value = new google.maps.Map(document.getElementById('map'), mapOptions)
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
.location-section {
  width: 100%;
}

.section-header {
  text-align: center;
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.section-title i {
  color: #4caf50;
  font-size: 1.2em;
}

.section-description {
  color: #666;
  font-size: 1.1rem;
}

.map-container {
  display: flex;
  gap: 1.5rem;
  height: 600px;
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.map-wrapper {
  flex: 1;
  position: relative;
  min-width: 0;
}

.map {
  width: 100%;
  height: 100%;
  border-radius: 16px 0 0 16px;
}

.map-overlay {
  position: absolute;
  top: 1rem;
  left: 1rem;
  z-index: 1;
}

.search-radius {
  background: rgba(255, 255, 255, 0.9);
  padding: 0.5rem 1rem;
  border-radius: 25px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-size: 0.9rem;
  color: #2c3e50;
}

.search-radius i {
  color: #4caf50;
}

.library-list {
  width: 350px;
  display: flex;
  flex-direction: column;
  background: white;
  border-left: 1px solid rgba(0, 0, 0, 0.08);
}

.list-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}

.list-header h3 {
  font-size: 1.2rem;
  color: #2c3e50;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.list-header i {
  color: #4caf50;
}

.list-content {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.no-results {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #666;
  gap: 1rem;
  text-align: center;
}

.no-results i {
  font-size: 2rem;
  color: #4caf50;
}

.library-item {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  transition: background-color 0.3s ease;
  gap: 1rem;
}

.library-item:hover {
  background-color: rgba(76, 175, 80, 0.05);
}

.library-info {
  flex: 1;
  min-width: 0;
  overflow: hidden;
}

.library-info h4 {
  margin: 0 0 0.5rem;
  font-size: 1rem;
  color: #2c3e50;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.vicinity {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0;
  font-size: 0.9rem;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.vicinity i {
  color: #4caf50;
  font-size: 0.8em;
  flex-shrink: 0;
}

.directions-button {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.5rem 0.75rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  text-decoration: none;
  transition: all 0.3s ease;
  white-space: nowrap;
  flex-shrink: 0;
}

.directions-button:hover {
  background-color: #43a047;
  transform: translateY(-2px);
}

@media (max-width: 1200px) {
  .map-container {
    height: 500px;
  }
}

@media (max-width: 992px) {
  .map-container {
    flex-direction: column;
    height: auto;
  }

  .map-wrapper {
    height: 400px;
  }

  .map {
    border-radius: 16px 16px 0 0;
  }

  .library-list {
    width: 100%;
    height: 300px;
    border-left: none;
    border-top: 1px solid rgba(0, 0, 0, 0.08);
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.3rem;
  }

  .section-description {
    font-size: 1rem;
  }

  .map-wrapper {
    height: 300px;
  }

  .library-list {
    height: 250px;
  }
}

@media (max-width: 480px) {
  .map-container {
    border-radius: 12px;
  }

  .map {
    border-radius: 12px 12px 0 0;
  }

  .search-radius {
    font-size: 0.8rem;
    padding: 0.4rem 0.8rem;
  }

  .library-item {
    padding: 0.75rem;
  }

  .directions-button {
    padding: 0.4rem 0.6rem;
    font-size: 0.8rem;
  }
}
</style>