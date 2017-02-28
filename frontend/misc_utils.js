export function formatAddress(restaurant) {
  const { boro, street, building, zipcode } = restaurant;
  return `${building} ${street} ${boro} ${zipcode}`;
}

export function capitalize(words) {
  return words.split(' ').map(capitalizeSingle).join(' ')
}

export function preview(string, maxLen) {
  return string.length > maxLen ? string.slice(0, maxLen) + "..." : string;
}

function capitalizeSingle(word) {
  if (word.length === 0) return ""
  return word[0].toUpperCase() + word.slice(1).toLowerCase();
}
