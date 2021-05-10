import * as React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { Box } from '@material-ui/core';
import ImageCard from '../components/ImageCard';
import UploadDialog from '../components/UploadDialog';
import DeleteDialog from '../components/DeleteDialog';
import SearchBar from '../components/SearchBar';
import ImageInfo from '../types/ImageInfo';
import axios from 'axios';
import { Grid } from '@material-ui/core';
import { Pagination } from '@material-ui/lab';
import MusicNoteIcon from '@material-ui/icons/MusicNote';

export default function Index() {
  const [rawImages, setRawImages] = React.useState<ImageInfo[]>([]);
  const [images, setImages] = React.useState<ImageInfo[]>([]);
  const [displayedImages, setDisplayedImages] = React.useState<ImageInfo[]>([]);
  const [selectedImageIds, setSelectedImageIds] = React.useState<number[]>([]);

  const [currentPage, setCurrentPage] = React.useState<number>(1);
  const ITEMS_PER_PAGE = 6;
  const numPages = Math.ceil(images.length / ITEMS_PER_PAGE);

  React.useEffect(() => {
    loadImages()
  }, [])

  React.useEffect(() => {
    // Handle pagination
    const page = currentPage - 1
    const maxIndex = images.length
    const startIndex = Math.min(page * ITEMS_PER_PAGE, maxIndex)
    const endIndex = Math.min(page * ITEMS_PER_PAGE + ITEMS_PER_PAGE, maxIndex)
    setDisplayedImages(images.slice(startIndex, endIndex))
    
  }, [currentPage, images])

  const loadImages = async () => {
    try {
      const res = await axios.get(`${process.env.NEXT_PUBLIC_API}/image/`);
      setCurrentPage(1);
      setSelectedImageIds([]);
      setRawImages(res.data);
      setImages(res.data);
    } catch {
      alert("Failed to load images")
    }
  }

  const handleSelectImage = (id: number) => {
    const imageIds = [...selectedImageIds] 
    if (imageIds.indexOf(id) != -1) {
      imageIds.splice(imageIds.indexOf(id), 1)
    } else {
      imageIds.push(id);
    }
    setSelectedImageIds(imageIds);
  }

  const handleSearch = (search: string) => {
    if (!search) {
      setImages(rawImages);
    } else {
      setImages(rawImages.filter(imageInfo => {
        return imageInfo.image_name.toLowerCase().includes(search.toLowerCase());
      }))
    }
  }

  return (
    <Container style={{paddingTop: "2em", paddingBottom: "2em"}}>
      <Box>
        <Box display="flex" flexDirection="column" justifyContent="center" alignItems="center">
          <Box display="flex" justifyContent="center" alignItems="center">
            <MusicNoteIcon style={{fontSize: '65px'}}/>
            <Typography variant="h4" component="h1">
              <em>A Thousand Notes</em>
            </Typography>
          </Box>
          <Box p={2} width='100%'>
            <SearchBar handleSearch={handleSearch}/>
          </Box>
          <Grid container justify="center">
            <UploadDialog loadImages={loadImages}/>
            <Box ml={2}>
              <DeleteDialog selectedImageIds={selectedImageIds} loadImages={loadImages}/>
            </Box>
          </Grid>
        </Box>
        <Grid container justify="center">
            {displayedImages.map((imageInfo: ImageInfo) => {
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
