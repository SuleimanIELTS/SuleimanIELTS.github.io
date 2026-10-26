// Audio Recorder Component for In-Browser IELTS Speaking Practice

class AudioRecorder {
  constructor(btnElemId, audioContainerId, timerElemId) {
    this.btnElem = document.getElementById(btnElemId);
    this.container = document.getElementById(audioContainerId);
    this.timerElem = document.getElementById(timerElemId);
    this.mediaRecorder = null;
    this.audioChunks = [];
    this.isRecording = false;
    this.elapsedSeconds = 0;
    this.counterInterval = null;

    if (this.btnElem) {
      this.btnElem.addEventListener("click", () => this.toggle());
    }
  }

  async toggle() {
    if (this.isRecording) {
      this.stop();
    } else {
      await this.start();
    }
  }

  async start() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.audioChunks = [];
      this.mediaRecorder = new MediaRecorder(stream);

      this.mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          this.audioChunks.push(e.data);
        }
      };

      this.mediaRecorder.onstop = () => {
        const audioBlob = new Blob(this.audioChunks, { type: "audio/webm" });
        const audioUrl = URL.createObjectURL(audioBlob);
        this.renderPlayer(audioUrl);
        stream.getTracks().forEach((track) => track.stop());
      };

      this.mediaRecorder.start();
      this.isRecording = true;
      this.elapsedSeconds = 0;
      this.updateBtnState();

      this.counterInterval = setInterval(() => {
        this.elapsedSeconds++;
        if (this.timerElem) {
          const mins = Math.floor(this.elapsedSeconds / 60);
          const secs = this.elapsedSeconds % 60;
          this.timerElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
        }
      }, 1000);
    } catch (err) {
      alert("Microphone access is required to record speaking answers. Please check browser permissions.");
      console.error("Microphone error:", err);
    }
  }

  stop() {
    if (!this.mediaRecorder) return;
    this.mediaRecorder.stop();
    this.isRecording = false;
    clearInterval(this.counterInterval);
    this.updateBtnState();
  }

  updateBtnState() {
    if (!this.btnElem) return;
    if (this.isRecording) {
      this.btnElem.classList.add("recording");
      this.btnElem.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <rect x="6" y="6" width="12" height="12" rx="2"></rect>
        </svg>
        <span>Stop Recording</span>
      `;
    } else {
      this.btnElem.classList.remove("recording");
      this.btnElem.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <circle cx="12" cy="12" r="7"></circle>
        </svg>
        <span>Record Speech</span>
      `;
    }
  }

  renderPlayer(url) {
    if (!this.container) return;
    this.container.innerHTML = `
      <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
        <audio controls src="${url}"></audio>
        <a href="${url}" download="ielts_speaking_answer.webm" class="btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.7rem;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" y1="15" x2="12" y2="3"></line>
          </svg>
          Save Audio
        </a>
      </div>
    `;
  }
}

window.AudioRecorder = AudioRecorder;
