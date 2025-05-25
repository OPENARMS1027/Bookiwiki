<template>
  <div class="voice-container" v-if="book">
    <div class="button-group">
      <button
        class="voice-button"
        @click="speakDescription"
        :disabled="isLoading || isPlaying"
      >
        <i class="fas fa-volume-up"></i>
        {{ isLoading ? '음성 생성 중...' : '책 설명 AI로 듣기' }}
      </button>

      <div class="control-buttons" v-if="audioUrl">
        <button class="control-button" @click="togglePlay">
          <i :class="isPlaying ? 'fas fa-pause' : 'fas fa-play'"></i>
        </button>
        <button class="control-button" @click="restartAudio">
          <i class="fas fa-redo"></i>
        </button>
        <button class="control-button" @click="stopAudio">
          <i class="fas fa-stop"></i>
        </button>
      </div>
    </div>
    <audio
      ref="audioPlayer"
      @ended="handleAudioEnd"
      @pause="handleAudioPause"
      @play="handleAudioPlay"
      style="display: none"
    ></audio>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const props = defineProps({
  book: Object,
})

const OPENAI_API_KEY = import.meta.env.VITE_OPENAI_API_KEY
const isLoading = ref(false)
const isPlaying = ref(false)
const audioPlayer = ref(null)
const audioUrl = ref(null)

const speakDescription = async () => {
  if (!props.book?.description || isLoading.value) return

  try {
    isLoading.value = true

    const response = await axios({
      method: 'POST',
      url: 'https://api.openai.com/v1/audio/speech',
      headers: {
        Authorization: `Bearer ${OPENAI_API_KEY}`,
        'Content-Type': 'application/json',
      },
      data: {
        model: 'tts-1',
        input: props.book.description,
        voice: 'alloy',
        response_format: 'mp3',
      },
      responseType: 'blob',
    })

    // Blob URL 생성 및 재생
    const audioBlob = new Blob([response.data], { type: 'audio/mpeg' })
    const url = URL.createObjectURL(audioBlob)

    audioUrl.value = url
    audioPlayer.value.src = url
    await audioPlayer.value.play()
    isPlaying.value = true
  } catch (error) {
    console.error('음성 생성 중 오류 발생:', error)
    alert('음성 생성에 실패했습니다.')
  } finally {
    isLoading.value = false
  }
}

const togglePlay = () => {
  if (audioPlayer.value) {
    if (isPlaying.value) {
      audioPlayer.value.pause()
    } else {
      audioPlayer.value.play()
    }
  }
}

const restartAudio = () => {
  if (audioPlayer.value) {
    audioPlayer.value.currentTime = 0
    audioPlayer.value.play()
    isPlaying.value = true
  }
}

const stopAudio = () => {
  if (audioPlayer.value) {
    audioPlayer.value.pause()
    audioPlayer.value.currentTime = 0
    isPlaying.value = false
  }
}

const handleAudioEnd = () => {
  isPlaying.value = false
  if (audioPlayer.value?.src) {
    audioPlayer.value.currentTime = 0
  }
}

const handleAudioPause = () => {
  isPlaying.value = false
}

const handleAudioPlay = () => {
  isPlaying.value = true
}
</script>

<style scoped>
.voice-container {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.button-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.voice-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.voice-button:hover:not(:disabled) {
  background-color: #45a049;
}

.voice-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.control-buttons {
  display: flex;
  gap: 10px;
}

.control-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background-color: #2196f3;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.control-button:hover {
  background-color: #1976d2;
}

.control-button i {
  font-size: 16px;
}
</style>
