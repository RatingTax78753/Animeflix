document.addEventListener('DOMContentLoaded', function () {
    const dropdownTemporada = document.getElementById('temporadaDropdown');
    const dropdownTipo = document.getElementById('tipoDropdown');
    const episodes = document.querySelectorAll('.episode-item');

    dropdownTemporada.addEventListener('change', filterEpisodes);
    dropdownTipo.addEventListener('change', filterEpisodes);

    function filterEpisodes() {
        const selectedTemporada = dropdownTemporada.value;
        const selectedTipo = dropdownTipo.value;

        episodes.forEach(episode => {
            const temporadaId = episode.getAttribute('data-temporada-id');
            const tipo = episode.getAttribute('data-tipo');

            const isTemporadaValid = selectedTemporada === 'all' || temporadaId === selectedTemporada;
            const isTipoValid = selectedTipo === 'all' || tipo === selectedTipo;

            if (isTemporadaValid && isTipoValid) {
                episode.style.display = 'block';
            } else {
                episode.style.display = 'none';
            }
        });
    }
});