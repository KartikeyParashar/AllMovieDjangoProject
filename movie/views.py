# Create your views here.
import logging

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from Lib.smd_response import SMD_Response
from movie.models import Actor, Producer, Movie
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


class GetAllActors(GenericAPIView):
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


class GetActorWithID(GenericAPIView):
    serializer_class = ActorSerializer

    def get(self, request, id, *args, **kwargs):
        """
        :param request: request for get the particular Actor Details
        :param id: Here, we pass an ID for update of a specific Actor Object
        :return: It will get a requested Actor with ID from the Database
        """
        try:
            # import pdb
            # pdb.set_trace()
            actor_data = Actor.objects.filter(id=id)
            if actor_data:
                serializer = ActorSerializer(actor_data, many=True)
                logger.info("Successfully Read Actor Details")
                smd = SMD_Response(status=True, message="Successfully Get the Requested Actor Details",
                                   data=[serializer.data])
                logger.info('Successfully Get Actor Details')
                return Response(smd, status=status.HTTP_200_OK)
            else:
                logger.error("No data available/invalid id")
                smd = SMD_Response(status=False, message="No Content Available",
                                   data=[])
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("Something went wrong" + str(e))
            smd = SMD_Response(status=False, message="Something Went Wrong")
            return Response(smd, status=status.HTTP_404_NOT_FOUND)


class UpdateActorDetailsWithID(GenericAPIView):
    serializer_class = ActorSerializer

    def put(self, request, id, *args, **kwargs):
        """
        :param request:Request for put(update) the Actor Details
        :param id:Here, we pass an ID for update of a specific Actor
        :return:It will update a requested Actor Object in Database
        """
        try:
            actor_obj = Actor.objects.get(id=id)
            if actor_obj is not None:
                data = request.data
                serializer = ActorSerializer(actor_obj, data=data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info("Successfully Updated the Details of the Actor")
                    smd = SMD_Response(status=True, message="Actors Details Successfully Updated",
                                       data=[serializer.data])
                    return Response(smd, status=status.HTTP_202_ACCEPTED)
                else:
                    logger.error("Please provide valid details")
                    smd = SMD_Response(message="Invalid Request/No such query exist",
                                       data=[serializer.errors])
                    return Response(smd, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.info("No DATA Present")
                return Response(SMD_Response(message="No Data Present"),
                                status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Please Provide a Valid ID or "
                                                 "Something Went Wrong"),
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteActorDetailsWithID(GenericAPIView):
    serializer_class = ActorSerializer

    def delete(self, request, id, *args, **kwargs):
        """
        :param request:Request for Delete Actor Details
        :param id: Here, we pass a ID for deleting requested Actor ID
        :return: This function delete the requested Actor Details from the DATABASE
        """
        try:
            actor_obj = Actor.objects.filter(id=id)
            if actor_obj:
                actor_obj.delete()
                logger.info("Actor Details Deleted")
                return Response(SMD_Response(status=True, message="Successfully Deleted the Actor Details"),
                                status=status.HTTP_204_NO_CONTENT)
            else:
                logger.error("Please provide valid details")
                smd = SMD_Response(message="Not found such Detail")
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Not a VALID ID or Something went wrong!!"),
                            status=status.HTTP_400_BAD_REQUEST)


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


class GetAllProducers(GenericAPIView):
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


class GetProducerWithID(GenericAPIView):
    serializer_class = ProducerSerializer

    def get(self, request, id, *args, **kwargs):
        """
        :param request: request for get the particular Producer Details
        :param id: Here, we pass an ID for update of a specific Producer Object
        :return: It will get a requested Producer with ID from the Database
        """
        try:
            # import pdb
            # pdb.set_trace()
            producer_data = Producer.objects.filter(id=id)
            if producer_data:
                serializer = ProducerSerializer(producer_data, many=True)
                logger.info("Successfully Read Producer Details")
                smd = SMD_Response(status=True, message="Successfully Get the Requested Producer Details",
                                   data=[serializer.data])
                logger.info('Successfully Get Producer Details')
                return Response(smd, status=status.HTTP_200_OK)
            else:
                logger.error("No data available/invalid id")
                smd = SMD_Response(status=False, message="No Content Available",
                                   data=[])
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("Something went wrong" + str(e))
            smd = SMD_Response(status=False, message="Something Went Wrong")
            return Response(smd, status=status.HTTP_404_NOT_FOUND)


class UpdateProducerDetailsWithID(GenericAPIView):
    serializer_class = ProducerSerializer

    def put(self, request, id, *args, **kwargs):
        """
        :param request:Request for put(update) the Producer Details
        :param id:Here, we pass an ID for update of a requested Producer
        :return:It will Update a requested Producer Details in Database
        """
        try:
            producer_obj = Producer.objects.get(id=id)
            if producer_obj is not None:
                data = request.data
                serializer = ProducerSerializer(producer_obj, data=data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info("Successfully Updated the Details of the Producer")
                    smd = SMD_Response(status=True, message="Producer Details Successfully Updated",
                                       data=[serializer.data])
                    return Response(smd, status=status.HTTP_202_ACCEPTED)
                else:
                    logger.error("Please provide valid details")
                    smd = SMD_Response(message="Invalid Request/No such query exist",
                                       data=[serializer.errors])
                    return Response(smd, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.info("No DATA Present")
                return Response(SMD_Response(message="No Data Present"),
                                status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Please Provide a Valid ID or "
                                                 "Something Went Wrong"),
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteProducerDetailsWithID(GenericAPIView):
    serializer_class = ProducerSerializer

    def delete(self, request, id, *args, **kwargs):
        """
        :param request:Request for Delete Producer Details
        :param id: Here, we pass a ID for deleting requested Producer ID
        :return: This function delete the requested Producer Details from the DATABASE
        """
        try:
            producer_obj = Producer.objects.filter(id=id)
            if producer_obj:
                producer_obj.delete()
                logger.info("Producer Details Deleted")
                return Response(SMD_Response(status=True, message="Successfully Deleted the Producer Details"),
                                status=status.HTTP_204_NO_CONTENT)
            else:
                logger.error("Please provide valid details")
                smd = SMD_Response(message="Not found such Detail")
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Not a VALID ID or Something went wrong!!"),
                            status=status.HTTP_400_BAD_REQUEST)


class AddMovie(GenericAPIView):
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        """

        :param request: request the movie details
        :return: save the details of a movie in database
        """
        try:
            # import pdb
            # pdb.set_trace()
            data = request.data
            if 'actor' in data:
                actor_list = []
                actors = data['actor']
                for name in actors:
                    obj = Actor.objects.get(actor_name=name)
                    if obj:
                        actor_list.append(obj.id)
                    else:
                        return Response(SMD_Response(message="Something went wrong when"
                                                             "while adding actors"))
                data['actor'] = actor_list
            if 'producer' in data:
                producer_list = []
                producers = data['producer']
                for name in producers:
                    obj = Producer.objects.get(producer_name=name)
                    if obj:
                        producer_list.append(obj.id)
                    else:
                        return Response(SMD_Response(message="Something went wrong when"
                                                             "while adding producers"))
                data['producer'] = producer_list
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


class GetAllMovies(GenericAPIView):
    serializer_class = ProducerSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request: Request for getting all the movie details
        :return: the details of all producers
        """
        try:
            all_movie = Movie.objects.all()
            if all_movie:
                serializer = MovieSerializer(all_movie, many=True)
                logger.info("Successfully get the movie details from the database")
                smd = SMD_Response(status=True, message="Successfully get the movie details from the database",
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


class GetMovieWithID(GenericAPIView):
    serializer_class = MovieSerializer

    def get(self, request, id, *args, **kwargs):
        """
        :param request: request for get the particular Movie Details
        :param id: Here, we pass an ID for update of a specific Movie Object
        :return: It will get a requested Movie with ID from the Database
        """
        try:
            # import pdb
            # pdb.set_trace()
            movie_data = Movie.objects.filter(id=id)
            if movie_data:
                serializer = MovieSerializer(movie_data, many=True)
                logger.info("Successfully Read Movie Details")
                smd = SMD_Response(status=True, message="Successfully Get the Requested Movie Details",
                                   data=[serializer.data])
                logger.info('Successfully Get Movie Details')
                return Response(smd, status=status.HTTP_200_OK)
            else:
                logger.error("No data available/invalid id")
                smd = SMD_Response(status=False, message="No Content Available",
                                   data=[])
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("Something went wrong" + str(e))
            smd = SMD_Response(status=False, message="Something Went Wrong")
            return Response(smd, status=status.HTTP_404_NOT_FOUND)


class UpdateMovieDetailsWithID(GenericAPIView):
    serializer_class = MovieSerializer

    def put(self, request, id, *args, **kwargs):
        """
        :param request:request for put(update) the Movie Details
        :param id:Here, we pass an ID for update of a requested Movie
        :return:It will Update a requested Movie Details in Database
        """
        try:
            # import pdb
            # pdb.set_trace()
            movie_obj = Movie.objects.get(id=id)
            if movie_obj is not None:
                data = request.data
                if 'actor' in data:
                    actor_list = []
                    actors = data['actor']
                    for name in actors:
                        obj = Actor.objects.get(actor_name=name)
                        if obj:
                            actor_list.append(obj.id)
                        else:
                            return Response(SMD_Response(message="Something went wrong when"
                                                                 "while adding actors"))
                    data['actor'] = actor_list
                if 'producer' in data:
                    producer_list = []
                    producers = data['producer']
                    for name in producers:
                        obj = Producer.objects.get(producer_name=name)
                        if obj:
                            producer_list.append(obj.id)
                        else:
                            return Response(SMD_Response(message="Something went wrong when"
                                                                 "while adding producers"))
                    data['producer'] = producer_list
                serializer = MovieSerializer(movie_obj, data=data)
                if serializer.is_valid():
                    serializer.save()
                    logger.info("Successfully Updated the Details of the a Movie")
                    smd = SMD_Response(status=True, message="Movie Details Successfully Updated",
                                       data=[serializer.data])
                    return Response(smd, status=status.HTTP_202_ACCEPTED)
                else:
                    logger.error("Please provide valid details")
                    smd = SMD_Response(message="Invalid Request/No such query exist",
                                       data=[serializer.errors])
                    return Response(smd, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.info("No DATA Present")
                return Response(SMD_Response(message="No Data Present"),
                                status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Please Provide a Valid ID or "
                                                 "Something Went Wrong"),
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteMovieDetailsWithID(GenericAPIView):
    serializer_class = MovieSerializer

    def delete(self, request, id, *args, **kwargs):
        """
        :param request:Request for Delete Movie Details
        :param id: Here, we pass a ID for deleting requested Movie ID
        :return: This function delete the requested Movie Details from the DATABASE
        """
        try:
            movie_obj = Movie.objects.filter(id=id)
            if movie_obj:
                movie_obj.delete()
                logger.info("Movie Details Deleted")
                return Response(SMD_Response(status=True, message="Successfully Deleted the Movie Details"),
                                status=status.HTTP_204_NO_CONTENT)
            else:
                logger.error("Please provide valid details")
                smd = SMD_Response(message="Not found such Detail")
                return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.warning("SOMETHING WENT WRONG" + str(e))
            return Response(SMD_Response(message="Not a VALID ID or Something went wrong!!"),
                            status=status.HTTP_400_BAD_REQUEST)
