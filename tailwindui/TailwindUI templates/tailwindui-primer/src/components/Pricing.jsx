import { ButtonLink } from '@/components/Button'
import { Container } from '@/components/Container'
import { GridPattern } from '@/components/GridPattern'
import { SectionHeading } from '@/components/SectionHeading'

export function Pricing() {
  return (
    <section
      id="pricing"
      aria-labelledby="pricing-title"
      className="scroll-mt-14 pt-16 pb-8 sm:scroll-mt-32 sm:pt-20 sm:pb-10 lg:pt-32 lg:pb-16"
    >
      <Container>
        <SectionHeading number="4" id="pricing-title">
          Pricing
        </SectionHeading>
        <p className="mt-8 font-display text-5xl font-extrabold tracking-tight text-slate-900 sm:text-6xl">
          Pick your package
        </p>
        <p className="mt-4 max-w-xl text-lg tracking-tight text-slate-600">
          “Everything Starts as a Square” is available in two different packages
          so you can pick the one that’s right for you.
        </p>
      </Container>
      <div className="mx-auto mt-16 max-w-5xl lg:px-6">
        <div className="grid bg-slate-50 sm:px-6 sm:pb-16 md:grid-cols-2 md:rounded-6xl md:px-8 md:pt-16 lg:p-20">
          <div className="flex flex-col px-4 py-16 sm:px-10 md:py-12 lg:px-12">
            <h3 className="mt-7 text-lg font-semibold tracking-tight text-slate-900">
              Essential
            </h3>
            <p className="mt-2 text-lg tracking-tight text-slate-600">
              The perfect starting point if you’re on a budget.
            </p>
            <p className="-order-1 flex font-display font-bold">
              <span className="text-[1.75rem] leading-tight text-slate-500">
                $
              </span>
              <span className="ml-1 mt-1 text-7xl tracking-tight text-slate-900">
                15
              </span>
            </p>
            <div className="order-1 mt-8">
              <ul className="-my-2 divide-y divide-slate-200 text-base tracking-tight text-slate-900">
                {[
                  'The 240-page ebook',
                  'Figma icon templates',
                  'Community access',
                ].map((feature) => (
                  <li key={feature} className="flex py-2">
                    <svg
                      aria-hidden="true"
                      className="h-8 w-8 flex-none fill-slate-600"
                    >
                      <path d="M11.83 15.795a1 1 0 0 0-1.66 1.114l1.66-1.114Zm9.861-4.072a1 1 0 1 0-1.382-1.446l1.382 1.446ZM14.115 21l-.83.557a1 1 0 0 0 1.784-.258L14.115 21Zm.954.3c1.29-4.11 3.539-6.63 6.622-9.577l-1.382-1.446c-3.152 3.013-5.704 5.82-7.148 10.424l1.908.598Zm-4.9-4.391 3.115 4.648 1.661-1.114-3.114-4.648-1.662 1.114Z" />
                    </svg>
                    <span className="ml-4">{feature}</span>
                  </li>
                ))}
              </ul>
            </div>
            <ButtonLink
              href="#"
              color="slate"
              className="mt-8"
              aria-label="Get started with the Icon Beginner plan for $15"
            >
              Get started
            </ButtonLink>
          </div>
          <div className="relative bg-blue-600 py-16 px-4 sm:rounded-5xl sm:py-12 sm:px-10 sm:shadow-lg lg:px-12">
            <div className="absolute inset-0 text-white/10 [mask-image:linear-gradient(white,transparent)]">
              <GridPattern x="50%" y="50%" />
            </div>
            <div className="relative flex flex-col">
              <h3 className="mt-7 text-lg font-semibold tracking-tight text-white">
                Complete
              </h3>
              <p className="mt-2 text-lg tracking-tight text-white">
                Everything icon resource you could ever ask for.
              </p>
              <p className="-order-1 flex font-display font-bold">
                <span className="text-[1.75rem] leading-tight text-blue-200">
                  $
                </span>
                <span className="ml-1 mt-1 text-7xl tracking-tight text-white">
                  229
                </span>
              </p>
              <div className="order-1 mt-8">
                <ul className="-my-2 divide-y divide-white/10 text-base tracking-tight text-white">
                  {[
                    'The 240-page ebook',
                    'Figma icon templates',
                    'Over an hour of screencasts',
                    'Weekly icon teardowns',
                    'Community access',
                  ].map((feature) => (
                    <li key={feature} className="flex py-2">
                      <svg aria-hidden="true" className="h-8 w-8 fill-white">
                        <path d="M11.83 15.795a1 1 0 0 0-1.66 1.114l1.66-1.114Zm9.861-4.072a1 1 0 1 0-1.382-1.446l1.382 1.446ZM14.115 21l-.83.557a1 1 0 0 0 1.784-.258L14.115 21Zm.954.3c1.29-4.11 3.539-6.63 6.622-9.577l-1.382-1.446c-3.152 3.013-5.704 5.82-7.148 10.424l1.908.598Zm-4.9-4.391 3.115 4.648 1.661-1.114-3.114-4.648-1.662 1.114Z" />
                      </svg>
                      <span className="ml-4">{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <ButtonLink
                href="#"
                color="white"
                className="mt-8"
                aria-label="Get started with the Icon Pro plan for $229"
              >
                Get started
              </ButtonLink>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
