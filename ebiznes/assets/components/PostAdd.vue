<template>
    <div>
        <router-link :to="{ name: 'posts' }">Post list</router-link>

        <div class="container-fluid">
            <div class="row">
                <div class="col-6">
                    <textarea v-model="content" class="form-control" placeholder="Post content"></textarea>
                </div>
                <div class="col-6">
                    <button @click="send" class="btn btn-primary">Send</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'PostAdd',
    data() {
        return {
            content: '',
        }
    },
    methods: {
        send: function() {
            axios.post('/posts/', {
                content: this.content,
            })
            .then(response => {
                this.$toastr.s('Post added');
            })
            .catch(response => {
                this.$toastr.e('Please try again later.')
            })
        }
    }
};
</script>

