from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
class CursoSerializer(serializers.ModelSerializer):

    # 1. Nested Relationship
        # - perfomático -> Pois gera todas as informações de relacionamento no request do GET (ex:tanto de cursos e avaliacões)
        # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2. Hyperlink Related Field
        # + perfomático pois ele gera um campo com o hyperlink / endpoint / URI
        # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3. Primary Key Related Field:
    # ++ perfomático pois ele informa a quantidade apenas , utilizado para sistemas com muitas cargas de acesso/registros
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )