<script>
	export let data;
</script>

<h1>Items:</h1>
<ul>
  {#each data.items as item}
    <li>{item.name}: {item.description}</li>
  {/each}
</ul>
