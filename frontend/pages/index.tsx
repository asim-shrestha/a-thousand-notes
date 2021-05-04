import * as React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { Box } from '@material-ui/core';

export default function Index() {
  return (
    <Container>
      <Box>
        <Typography variant="h4" component="h1">
          Test
        </Typography>
      </Box>
    </Container>
  );
}
