import graphene

from graphene_django.types import DjangoObjectType

from .models import Language, Artist, Album, Track


class LanguageType(DjangoObjectType):
    class Meta:
        model = Language


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(object):
    all_languages = graphene.List(LanguageType)
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)
    all_tracks = graphene.List(TrackType)

    def resolve_all_languages(self, info, **kwargs):
        return Language.objects.all()

    def resolve_all_tracks(self, info, **kwargs):
        return Track.objects.all()

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()
        
