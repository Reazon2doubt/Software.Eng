document.addEventListener("DOMContentLoaded", () => {

    const submitBtn = document.getElementById("submitBtn");
    const results = document.getElementById("results");

    submitBtn.addEventListener("click", () => {

        let score = 0;

        const answers = [
            document.querySelector('input[name="q1"]:checked'),
            document.querySelector('input[name="q2"]:checked')
        ];

        answers.forEach(answer => {
            if (answer && answer.value === "correct") {
                score++;
            }
        });

        const percentage =
            Math.round((score / answers.length) * 100);

        let feedback = "";

        if (percentage >= 80) {
            feedback = "Excellent understanding.";
        } else if (percentage >= 50) {
            feedback = "Good progress. Review a few concepts.";
        } else {
            feedback = "Further study recommended.";
        }

        results.innerHTML = `
            <p>Score: ${score}/${answers.length}</p>
            <p>${percentage}%</p>
            <p>${feedback}</p>
        `;
    });

});

const qrContainer = document.getElementById("qr-container");
const qrOverlay = document.getElementById("qr-overlay");

qrContainer.addEventListener("click", () => {

    qrContainer.classList.toggle("active");
    qrOverlay.classList.toggle("active");

});

qrOverlay.addEventListener("click", () => {

    qrContainer.classList.remove("active");
    qrOverlay.classList.remove("active");

});
