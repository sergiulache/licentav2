<script>
    
</script>

<main>
    <div id="wholePage" class="w-screen h-screen flex flex-row justify-center items-center"
    >
        <div id="imageBox" class=" rounded-xl border-4 border-neutral-800 shadow-lg flex mx-auto px-4 max-w-md bg-scroll bg-cover bg-no-repeat"
        >
        <slot/>
        </div>
    </div>
</main>

<style>
    /* set backgroud image to /static/formBackground.png */
    #imageBox {
        background-image: url('/formBackground.jpg');
    }    
</style>