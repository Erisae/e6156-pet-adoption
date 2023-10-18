from fastapi import FastAPI, HTTPException
from typing import List

import uvicorn
from resources.adoptions.adoption_resource import AdoptionsResource
from resources.adoptions.adoption_data_service import AdoptionDataService
from resources.adoptions.adoption_models import AdoptionModel, AdoptionRspModel

app = FastAPI()

# This function returns a DataService instance.
def get_adoption_data_service():
    config = {
        "data_directory": "./data/",
        "data_file": "adoptions.json"
    }
    ds = AdoptionDataService(config)
    return ds

# This function returns a Resource instance, which will be used to handle API calls.
def get_adoption_resource():
    ds = get_adoption_data_service()
    config = {"data_service": ds}
    res = AdoptionsResource(config)
    return res

adoptions_resource = get_adoption_resource()

@app.get("/adoptions", response_model=List[AdoptionRspModel])
async def get_adoptions():
    """Return a list of all adoption requests."""
    result = adoptions_resource.get_adoptions()
    return result

@app.get("/adoptions/{adoptionId}", response_model=AdoptionRspModel)
async def get_adoption_by_id(adoptionId: str):
    """Retrieve adoption details by ID."""
    adoption = adoptions_resource.get_adoption_by_id(adoptionId)
    if not adoption:
        raise HTTPException(status_code=404, detail="Adoption not found")
    return adoption

@app.post("/adoptions", response_model=AdoptionRspModel)
async def create_adoption(adoption: AdoptionModel):
    """Create a new adoption request."""
    return adoptions_resource.create_adoption(adoption)

@app.put("/adoptions/{adoptionId}", response_model=AdoptionRspModel)
async def update_adoption(adoptionId: str, updated_data: AdoptionModel):
    """Shelter updates adoption status."""
    updated_adoption = adoptions_resource.update_adoption(adoptionId, updated_data)
    if not updated_adoption:
        raise HTTPException(status_code=404, detail="Adoption not found")
    return updated_adoption

@app.delete("/adoptions/{adoptionId}")
async def delete_adoption(adoptionId: str):
    """Delete an adoption request."""
    success = adoptions_resource.delete_adoption(adoptionId)
    if not success:
        raise HTTPException(status_code=404, detail="Adoption not found")
    return {"status": "Adoption deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
