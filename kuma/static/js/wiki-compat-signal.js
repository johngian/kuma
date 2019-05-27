(function() {
    'use strict';

    var bcdContainer;

    /**
     * Creates and returns the signal link HTML
     * @returns signal link HTML
     */
    function signalLink() {
        var container = document.createElement('div');
        var signalLink = document.createElement('a');
        signalLink.setAttribute('href', location.pathname + '$bcd-signal');
        signalLink.textContent = 'Is something wrong?';
        container.setAttribute('class', 'signal-link-container');
        container.appendChild(signalLink);
        return container;
    }

    bcdContainer = document.querySelector('.bc-data');
    bcdContainer.insertAdjacentElement('beforeend', signalLink());
})();
