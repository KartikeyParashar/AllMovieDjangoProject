# Create your views here.
import logging

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from Lib.smd_response import SMD_Response
from movie.models import Actor, Producer
from movie.serializers import MovieSerializer, ActorSerializer, ProducerSerializer

logger = logging.getLogger(__name__)


class AddActor(GenericAPIView):
    serializer_class = ActorSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: request the details of an actor
        :return: save the details of an actor in database
        """
        try:
            serializer = ActorSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("Successfully Save the actor details in the database")
                smd = SMD_Response(status=True, message="Successfully Save the actor details in the database",
                                   data=[serializer.data])
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                logger.error("Please Provide Valid Details")
                smd = SMD_Response(status=False, message="Please Provide Valid Details",
                                   data=[serializer.errors])
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Something went wrong-" + str(e))
            smd = SMD_Response(message="Something Went Wrong")
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)


class GetAllActor(GenericAPIView):
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request: Request for getting all the actor details
        :return: the details of all actors
        """
        try:
            all_actors = Actor.objects.all()
            if all_actors:
                serializer = ActorSerializer(all_actors, many=True)
                logger.info("Successfully get the actor details from the database")
                smd = SMD_Response(status=True, message="Successfully get the actor details from the database",
                                   data=[serializer.data])
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                logger.error("No data available to be fetch from DATABASE")
                smd = SMD_Response(status=False, message="No Content Available")
                return Response(smd, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.warning("Something went wrong-" + str(e))
            smd = SMD_Response(message="Something went wrong")
            return Response(smd, status=status.HTTP_404_NOT_FOUND)


class AddProducer(GenericAPIView):
    serializer_class = ProducerSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: request the details of a producer
        :return: save the details of a producer in database
        """
        try:
            serializer = ProducerSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("Successfully Save the producer details in the database")
                smd = SMD_Response(status=True, message="Successfully Save the producer details in the database",
                                   data=[serializer.data])
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                logger.error("Please Provide Valid Details")
                smd = SMD_Response(status=False, message="Please Provide Valid Details",
                                   data=[serializer.errors])
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Something went wrong-" + str(e))
            smd = SMD_Response(message="Something Went Wrong")
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)


class GetAllProducer(GenericAPIView):
    serializer_class = ProducerSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request: Request for getting all the producer details
        :return: the details of all producers
        """
        try:
            all_producers = Producer.objects.all()
            if all_producers:
                serializer = ProducerSerializer(all_producers, many=True)
                logger.info("Successfully get the producer details from the database")
                smd = SMD_Response(status=True, message="Successfully get the producer details from the database",
                                   data=[serializer.data])
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                logger.error("No data available to be fetch from DATABASE")
                smd = SMD_Response(status=False, message="No Content Available")
                return Response(smd, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.warning("Something went wrong-" + str(e))
            smd = SMD_Response(message="Something went wrong")
            return Response(smd, status=status.HTTP_404_NOT_FOUND)


class AddMovie(GenericAPIView):
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: request the movie details
        :return: save the details of a movie in database
        """
        try:
            serializer = MovieSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("Successfully Save the movie details in the database")
                smd = SMD_Response(status=True, message="Successfully Save the movie details in the database",
                                   data=[serializer.data])
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                logger.error("Please Provide Valid Details")
                smd = SMD_Response(status=False, message="Please Provide Valid Details",
                                   data=[serializer.errors])
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Something went wrong-" + str(e))
            smd = SMD_Response(message="Something Went Wrong")
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)
