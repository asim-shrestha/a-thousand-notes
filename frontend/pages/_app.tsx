import * as React from 'react';
import Head from 'next/head';
import { AppProps } from 'next/app';
import { ThemeProvider } from '@material-ui/core/styles';
import { CacheProvider } from '@emotion/react';
import CssBaseline from '@material-ui/core/CssBaseline';
import createCache from '@emotion/cache';
import theme from '../components/theme';
import { Box } from '@material-ui/core';

export const cache = createCache({ key: 'css', prepend: true });

export default function MyApp(props: AppProps) {
  const { Component, pageProps } = props;

  React.useEffect(() => {
    // Remove the server-side injected CSS.
    const jssStyles = document.querySelector('#jss-server-side');
    if (jssStyles) {
      jssStyles.parentElement!.removeChild(jssStyles);
    }
  }, []);

  return (
    <CacheProvider value={cache}>
      <Head>
        <title>A Thousand Notes</title>
        <meta name="viewport" content="initial-scale=1, width=device-width" />
        <link rel="shortcut icon" href="https://static.thenounproject.com/png/182706-200.png" />
      </Head>
      <ThemeProvider theme={theme}>
        {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
        <CssBaseline />
        <Box minWidth="100vw" minHeight="100vh" bgcolor={theme.palette.secondary.main}>
          <Component {...pageProps} />
        </Box>
      </ThemeProvider>
    </CacheProvider>
  );
}
