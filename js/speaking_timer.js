// Speaking Timer Module with Web Audio API Chime & Visual Countdown

class SpeakingTimer {
  constructor(displayElemId, defaultSeconds, onFinishCallback) {
    this.displayElem = document.getElementById(displayElemId);
    this.defaultSeconds = defaultSeconds;
    this.remainingSeconds = defaultSeconds;
    this.timerId = null;
    this.isRunning = false;
    this.onFinish = onFinishCallback;
    this.render();
  }

  start() {
    if (this.isRunning) return;
    this.isRunning = true;

    this.timerId = setInterval(() => {
      this.remainingSeconds--;
      this.render();

      if (this.remainingSeconds <= 0) {
        this.stop();
        this.playChime();
        if (typeof this.onFinish === "function") {
          this.onFinish();
        }
      }
    }, 1000);
  }

  pause() {
    this.isRunning = false;
    clearInterval(this.timerId);
    this.timerId = null;
  }

  reset(newSeconds = null) {
    this.pause();
    this.remainingSeconds = newSeconds !== null ? newSeconds : this.defaultSeconds;
    this.render();
  }

  render() {
    if (!this.displayElem) return;
    const mins = Math.floor(this.remainingSeconds / 60);
    const secs = this.remainingSeconds % 60;
    this.displayElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    // Color cue for final 15 seconds
    if (this.remainingSeconds <= 15 && this.remainingSeconds > 0) {
      this.displayElem.style.color = 'var(--accent-rose)';
    } else {
      this.displayElem.style.color = 'var(--text-primary)';
    }
  }

  playChime() {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
      osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.2); // A5

      gain.gain.setValueAtTime(0.3, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.6);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.6);
    } catch (e) {
      console.warn("Audio chime failed to play", e);
    }
  }
}

window.SpeakingTimer = SpeakingTimer;
