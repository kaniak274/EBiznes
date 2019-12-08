<template>
    <div class="text-center">
        <div class="mapouter">
            <div class="gmap_canvas">
                <iframe
                    width="600"
                    height="500"
                    id="gmap_canvas"
                    src="https://maps.google.com/maps?q=%C5%82%C3%B3d%C5%BA%2C%20piotrkowska%2016&t=&z=13&ie=UTF8&iwloc=&output=embed"
                    frameborder="0"
                    scrolling="no"
                    marginheight="0"
                    marginwidth="0">
                </iframe>
            </div>
        </div>

        <b style="font-size: 3em;">ServiceRent</b>
        <br/>Piotrkowska 16
        <br/>tel. 666 666 666
        <br/>REGON: 896106664
        <br/> NIP: 8126149201
    </div>
</template>
<script>
export default {
    name: 'Contact',
}
</script>
