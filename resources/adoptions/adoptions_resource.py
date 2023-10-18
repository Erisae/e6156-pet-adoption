from resources.abstract_base_resource import BaseResource
from resources.adoptions.adoption_models import AdoptionRspModel, AdoptionModel
from resources.rest_models import Link
from typing import List
from flask_restful import reqparse

class AdoptionResource(BaseResource):
    #
    # Initial setup for the Adoption resource.
    #

    def __init__(self, config):
        super().__init__()
        self.data_service = config["data_service"]

        # Setting up the request parser
        self.request_parser = reqparse.RequestParser()
        self.request_parser.add_argument('petId', type=str, required=True, help='Pet ID is required')
        self.request_parser.add_argument('adopterId', type=str, required=True, help='Adopter ID is required')

    @staticmethod
    def _generate_links(a: dict) -> AdoptionRspModel:
        self_link = Link(**{
            "rel": "self",
            "href": "/adoptions/" + a['adoptionId']
        })
        pet_link = Link(**{
            "rel": "pet",
            "href": "/pets/" + a['petId']
        })
        adopter_link = Link(**{
            "rel": "adopter",
            "href": "/users/" + a['adopterId']
        })

        links = [
            self_link,
            pet_link,
            adopter_link
        ]
        rsp = AdoptionRspModel(**a, links=links)
        return rsp

    def get_adoptions(self, adoption_id: str = None, pet_id: str = None, adopter_id: str = None) -> List[AdoptionRspModel]:
        result = self.data_service.get_adoptions(adoption_id, pet_id, adopter_id)
        final_result = []

        for a in result:
            m = self._generate_links(a)
            final_result.append(m)

        return final_result

       # POST /adoptions
    def post(self) -> AdoptionRspModel:
        data = self.request_parser.parse_args()  # Assuming you've defined a request_parser
        new_adoption = self.data_service.create_adoption(data)
        return self._generate_links(new_adoption)

    # GET /adoptions
    def get(self) -> List[AdoptionRspModel]:
        return self.get_adoptions()

    # GET /adoptions/{adoptionId}
    def get_adoption_by_id(self, adoption_id: str) -> AdoptionRspModel:
        adoption = self.data_service.get_adoption_by_id(adoption_id)
        if not adoption:
            raise NotFoundError(f"Adoption with ID {adoption_id} not found")  # Assuming you've defined NotFoundError
        return self._generate_links(adoption)

    # PUT /adoptions/{adoptionId}
    def put(self, adoption_id: str) -> AdoptionRspModel:
        data = self.request_parser.parse_args()
        updated_adoption = self.data_service.update_adoption_status(adoption_id, data)
        if not updated_adoption:
            raise NotFoundError(f"Adoption with ID {adoption_id} not found")
        return self._generate_links(updated_adoption)

    # DELETE /adoptions/{adoptionId}
    def delete(self, adoption_id: str):
        self.data_service.delete_adoption(adoption_id)
        return {}, 204  # Return a no-content response for successful delete
