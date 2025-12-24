async function loadDags() {
const res = await fetch('http://localhost:8000/dags');
const data = await res.json();


let html = '<ul>';
data.dags.forEach(dag => {
html += `<li>${dag.dag_id} — ${dag.is_paused ? 'Paused' : 'Active'}</li>`;
});
html += '</ul>';


document.getElementById('output').innerHTML = html;
}