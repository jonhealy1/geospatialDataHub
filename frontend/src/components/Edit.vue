/* eslint-disable */

<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="subscription.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter name"
                    :class="{'is-invalid': errors.has('subscription.name') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <!----->
            <div class="form-group">
                <label for="area">Area</label>
                <input
                    type="number"
                    class="form-control"
                    id="area"
                    v-model="subscription.area"
                    v-validate="'required'"
                    name="area"
                    placeholder="Enter area"
                    :class="{'is-invalid': errors.has('subscription.area') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid area.
                </div>
            </div>
            <!---
            ('pop2005', models.IntegerField(verbose_name='Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name='FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name='2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(verbose_name='United Nations Code')),
                ('region', models.IntegerField(verbose_name='Region Code')),
                ('subregion', models.IntegerField(verbose_name='Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            
            -->
            <div class="form-group">
                <label for="pop2005">Population 2005</label>
                <input
                    type="number"
                    class="form-control"
                    id="pop2005"
                    v-model="subscription.pop2005"
                    v-validate="'required'"
                    name="pop2005"
                    placeholder="Enter population"
                    :class="{'is-invalid': errors.has('subscription.pop2005') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid pop.
                </div>
            </div>
            <div class="form-group">
                <label for="fips">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="fips"
                    v-model="subscription.fips"
                    v-validate="'required'"
                    name="fips"
                    placeholder="Enter fips code"
                    :class="{'is-invalid': errors.has('subscription.fips') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid fips code.
                </div>
            </div>
            <div class="form-group">
                <label for="iso2">ISO 2</label>
                <input
                    type="text"
                    class="form-control"
                    id="iso2"
                    v-model="subscription.iso2"
                    v-validate="'required'"
                    name="iso2"
                    placeholder="Enter population"
                    :class="{'is-invalid': errors.has('subscription.iso2') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid iso2.
                </div>
            </div>
            <div class="form-group">
                <label for="iso3">ISO 3</label>
                <input
                    type="text"
                    class="form-control"
                    id="iso3"
                    v-model="subscription.iso3"
                    v-validate="'required'"
                    name="iso3"
                    placeholder="Enter population"
                    :class="{'is-invalid': errors.has('subscription.iso3') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid iso3.
                </div>
            </div>
            <div class="form-group">
                <label for="un">United Nations Code</label>
                <input
                    type="number"
                    class="form-control"
                    id="un"
                    v-model="subscription.un"
                    v-validate="'required'"
                    name="un"
                    placeholder="Enter United Nations Code"
                    :class="{'is-invalid': errors.has('subscription.un') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid United Nations Code.
                </div>
            </div>
            <div class="form-group">
                <label for="region">Region</label>
                <input
                    type="number"
                    class="form-control"
                    id="region"
                    v-model="subscription.region"
                    v-validate="'required'"
                    name="region"
                    placeholder="Enter region"
                    :class="{'is-invalid': errors.has('subscription.region') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid region.
                </div>
            </div>
            <div class="form-group">
                <label for="subregion">Sub Region</label>
                <input
                    type="number"
                    class="form-control"
                    id="subregion"
                    v-model="subscription.subregion"
                    v-validate="'required'"
                    name="subregion"
                    placeholder="Enter sub region"
                    :class="{'is-invalid': errors.has('subscription.rsubegion') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid sub region.
                </div>
            </div>
            <div class="form-group">
                <label for="lon">Longitude</label>
                <input
                    type="number"
                    class="form-control"
                    id="lon"
                    v-model="subscription.lon"
                    v-validate="'required'"
                    name="lon"
                    placeholder="Enter longitude"
                    :class="{'is-invalid': errors.has('subscription.lon') && submitted}">
                <div class="invalid-feedback">
                    Please provide a longitude.
                </div>
            </div>
            <div class="form-group">
                <label for="lat">Latitude</label>
                <input
                    type="number"
                    class="form-control"
                    id="lat"
                    v-model="subscription.lat"
                    v-validate="'required'"
                    name="lat"
                    placeholder="Enter latitude"
                    :class="{'is-invalid': errors.has('subscription.lat') && submitted}">
                <div class="invalid-feedback">
                    Please provide a latitude.
                </div>
            </div>
            <!-- <div class="form-group">
                <label for="mpoly">MultiPolygonField</label>
                <input
                    type="number"
                    class="form-control"
                    id="mpoly"
                    v-model="subscription.mpoly"
                    v-validate="'required'"
                    name="MultiPolygonField"
                    placeholder="Enter MultiPolygonField"
                    :class="{'is-invalid': errors.has('subscription.mpoly') && submitted}">
                <div class="invalid-feedback">
                    Please provide a MultiPolygonField.
                </div>
            </div> -->
            <!-- <div class="form-group">
                <label for="description">Description</label>
                <textarea
                    name="description"
                    class="form-control"
                    id="description"
                    v-validate="'required'"
                    v-model="subscription.description"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('subscription.description') && submitted}"></textarea>
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div> -->
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            subscription: {
                name: '',
                area: '',
                pop2005: '',
                fips: '',
                iso2: '',
                iso3: '',
                un: '',
                region: '',
                subregion: '',
                lon: '',
                lat: '',
                //mpoly: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/subscriptions/' + this.$route.params.id)
            .then( response => {
                console.log(response.data)
                this.subscription = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/subscriptions/${this.subscription.id}/`,
                        this.subscription
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>