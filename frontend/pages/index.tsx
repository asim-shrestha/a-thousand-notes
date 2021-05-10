import * as React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { Box } from '@material-ui/core';
import ImageCard from '../components/ImageCard';
import UploadDialog from '../components/UploadDialog';
import DeleteDialog from '../components/DeleteDialog';
import ImageInfo from '../types/ImageInfo';
import axios from 'axios';
import { Grid } from '@material-ui/core';
import { Pagination } from '@material-ui/lab';

export default function Index() {
  const [images, setImages] = React.useState<ImageInfo[]>([]);
  const [displayedImages, setDisplayedImages] = React.useState<ImageInfo[]>([]);
  const [selectedImageIds, setSelectedImageIds] = React.useState<string[]>([]);

  const [currentPage, setCurrentPage] = React.useState<number>(1);
  const ITEMS_PER_PAGE = 6;
  const numPages = Math.floor(images.length / ITEMS_PER_PAGE) + 1;


  React.useEffect(() => {
    loadImages()
  }, [])

  React.useEffect(() => {
    // Handle pagination
    const page = currentPage - 1
    const maxIndex = images.length ? images.length - 1 : 0 // Ensure we don't get -1
    const startIndex = Math.max(Math.min(page * ITEMS_PER_PAGE - 1, maxIndex) , 0)
    const endIndex = Math.min(page * ITEMS_PER_PAGE + ITEMS_PER_PAGE, maxIndex)
    setDisplayedImages(images.slice(startIndex, endIndex))
    console.log(startIndex, endIndex);
    
  }, [currentPage, images])

  const loadImages = async () => {
    try {
      const res = await axios.get(`${process.env.NEXT_PUBLIC_API}/image/`);
      setCurrentPage(1);
      setImages(res.data);
    } catch {
      alert("Failed to load images")
    }
  }

  const handleSelectImage = (id: string) => {
    const imageIds = [...selectedImageIds] 
    if (imageIds.indexOf(id) != -1) {
      imageIds.splice(imageIds.indexOf(id), 1)
    } else {
      imageIds.push(id);
    }
    setSelectedImageIds(imageIds);
  }

  return (
    <Container>
      <Box>
        <Typography variant="h4" component="h1">
          Test
        </Typography>
        <UploadDialog loadImages={loadImages}/>
        <DeleteDialog selectedImageIds={selectedImageIds} loadImages={loadImages}/>
        <Grid container justify="center">
            {displayedImages.map((imageInfo: ImageInfo) => {
              console.log(selectedImageIds.indexOf(imageInfo.id) != -1);
              
              return <ImageCard key={imageInfo.id} imageInfo={imageInfo} checked={selectedImageIds.indexOf(imageInfo.id) != -1} handleChecked={handleSelectImage}/>
            })}
        </Grid>
        <Grid container justify="center">
          <Pagination
            count={numPages}
            color="primary"
            page={currentPage}
            onChange={(e, page) => setCurrentPage(page)}
            size="large"
          />
        </Grid>
      </Box>
    </Container>
  );
}
