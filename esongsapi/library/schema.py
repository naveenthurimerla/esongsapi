import graphene

from graphene_django.types import DjangoObjectType

from .models import Language, Artist, Album, Track, Company, Genre, Lyric


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


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class LyricType(DjangoObjectType):
    class Meta:
        model = Lyric


class Query(object):
    
    language = graphene.Field(LanguageType, id=graphene.Int())
    artist = graphene.Field(ArtistType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    track = graphene.Field(TrackType, id=graphene.Int())
    genre = graphene.Field(GenreType, id=graphene.Int())
    company = graphene.Field(CompanyType, id=graphene.Int())
    lyric = graphene.Field(LyricType, id=graphene.Int())


    all_languages = graphene.List(LanguageType)
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)
    all_tracks = graphene.List(TrackType)
    all_genres = graphene.List(GenreType)
    all_companies = graphene.List(CompanyType)
    all_lyrics = graphene.List(LyricType)

    def resolve_language(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Language.objects.get(pk=id)

        return None
    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artist.objects.get(pk=id)

        return None
    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None        
    def resolve_track(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Track.objects.get(pk=id)

        return None
    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Genre.objects.get(pk=id)

        return None        

    def resolve_lyric(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Lyric.objects.get(pk=id)

        return None 
    
    def resolve_all_languages(self, info, **kwargs):
        return Language.objects.all()

    def resolve_all_tracks(self, info, **kwargs):
        return Track.objects.all()

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_all_lyrics(self, info, **kwargs):
        return Lyric.objects.all()
