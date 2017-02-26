export function fetchCuisines() {
  return fetch('/api/cuisines').then(response => response.json());
}

export function fetchCuisineStats(cuisine) {
  const queryString = "?cuisine=" + encodeURIComponent(cuisine)
  return fetch(`/api/cuisines/stats/${queryString}`).then(
    response => response.json()
  );
}
