import * as React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { Box } from '@material-ui/core';
import ImageCard from '../components/ImageCard';
import UploadDialog from '../components/UploadDialog';
import ImageInfo from '../types/ImageInfo';
import axios from 'axios';

export default function Index() {
  const [images, setImages] = React.useState<ImageInfo[]>([]);
  React.useEffect(() => {
    loadImages()
  }, [])

  const loadImages = async () => {
    try {
      const res = await axios.get(`${process.env.NEXT_PUBLIC_API}/image/`);
      setImages(res.data);
    } catch {
      alert("Failed to load images")
    }
  }

  return (
    <Container>
      <Box>
        <Typography variant="h4" component="h1">
          Test
        </Typography>
        <UploadDialog loadImages={loadImages}/>
        <Container>
          {images.map((imageInfo: ImageInfo) => {
            return <ImageCard key={imageInfo.id} imageInfo={imageInfo}/>
          })}
        </Container>
      </Box>
    </Container>
  );
}
