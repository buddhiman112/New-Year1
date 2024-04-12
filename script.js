// Get the current date and time
const now = new Date();
const newYear = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1); // Tomorrow's date

// Countdown timer function
function updateCountdown() {
	const diff = newYear - now;
	const days = Math.floor(diff / (1000 * 60 * 60 * 24));
	const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
	const seconds = Math.floor((diff % (1000 * 60)) / 1000);

	document.getElementById('countdown').innerHTML = `Countdown: ${days}d ${hours}h ${minutes}m ${seconds}s`;

	if (diff <= 0) {
		clearInterval(timer);
		document.getElementById('countdown').innerHTML = "Happy New Year!";
		document.getElementById('audio').play();
	}
}

// Update countdown every second
const timer = setInterval(updateCountdown, 1000);