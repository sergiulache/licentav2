  <script>
    export let data;
    let { items } = data;
    $: ({ items } = data);
  </script>

  <ul>
    {#each items as item}
      <li>{item.name}</li>
      
    {/each}
  </ul>
  