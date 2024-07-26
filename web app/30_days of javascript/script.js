document.addEventListener('DOMContentLoaded', () => {
    const quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Get busy living or get busy dying. - Stephen King",
        "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The best way to predict the future is to invent it. - Alan Kay",
        "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt"
    ];

    const quoteElement = document.getElementById('quote');
    const quoteButton = document.getElementById('quote-button');

    function getRandomQuote() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        return quotes[randomIndex];
    }

    quoteButton.addEventListener('click', () => {
        quoteElement.textContent = getRandomQuote();
    });
});

