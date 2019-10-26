<template>
    <div>
        <router-link :to="{ name: 'post-add' }">Add post</router-link>

        <div class="container-fluid">
            <div v-for="post in posts" :key="post.id">
                <div class="card mb-2">
                    <div class="card-header">
                        <button type="button" class="close" aria-label="Close" @click="remove(post.id)">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="card-body">
                        {{ post.content }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'PostList',
    data () {
        return {
            posts: [],
        }
    },
    created() {
        axios.get('posts/')
            .then(({ data }) => {
                this.posts = data;
            })
            .catch(response => {
                this.$toastr.e('Please try again later.');
            })
    },
    methods: {
        remove: function(post_id) {
            axios.delete(`posts/${post_id}/`)
                .then(response => {
                    this.posts = this.posts.filter(({ id }) => post_id !== id);
                    this.$toastr.s('Post deleted');
                })
                .catch(response => {
                    this.$toastr.e('Please try again later.');
                })
        }
    },
};
</script>
