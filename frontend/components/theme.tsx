import { createMuiTheme } from '@material-ui/core/styles';
import { red } from '@material-ui/core/colors';

// Create a theme instance.
const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#008060',
    },
    secondary: {
      main: '#fbf7ed',
    },
    error: {
      main: '#c7432c',
    },
    background: {
      default: '#fff',
    },
  },
});

export default theme;
