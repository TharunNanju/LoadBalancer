function refreshContainer() {
    fetch('/')
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const newContainerName = doc.querySelector('#container-name').textContent;
            document.getElementById('container-name').textContent = newContainerName;
        })
        .catch(error => console.error('Error refreshing:', error));
}