import * as React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { Box, Button } from '@material-ui/core';
import ImageCard from '../components/ImageCard';

export default function Index() {
  return (
    <Container>
      <Box>
        <Typography variant="h4" component="h1">
          Test
        </Typography>
        <Button size="large" variant="contained">Upload</Button>
        <Container>
          <ImageCard/>
          <ImageCard/>
        </Container>
      </Box>
    </Container>
  );
}
