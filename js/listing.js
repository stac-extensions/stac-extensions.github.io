(async () => {
  const repo = window.location.href.split('/').slice(-2).shift()
  const response = await fetch(`https://api.github.com/repos/stac-extensions/${repo}/git/trees/gh-pages?recursive=true`);
  const data = await response.json();
  schemas = data.tree.filter(f => {
    if (f.path.startsWith('v') && f.path.endsWith('json')) {
      return true
    }
  })
  let htmlString = `<h1>STAC Extension '${repo}' Schemas</h1><ul>`;
  for (let s of schemas) {
    htmlString += `<li><a href="${s.path}">${s.path}</a></li>`;
  }
  htmlString += '</ul>';
  document.getElementsByTagName('body')[0].innerHTML = htmlString;
})()
